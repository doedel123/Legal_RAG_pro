import os
import sys
import re
from dotenv import load_dotenv
from google import genai


def get_client():
    load_dotenv(".env.local", override=True)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Fehler: GEMINI_API_KEY nicht in .env.local gefunden.")
        sys.exit(1)
    return genai.Client(api_key=api_key)


def list_stores(client):
    stores = list(client.file_search_stores.list())
    if not stores:
        print("\nKeine Filestores vorhanden.")
        return stores

    print(f"\nVorhandene Filestores ({len(stores)}):")
    for i, s in enumerate(stores, 1):
        dn = getattr(s, "display_name", "") or "(ohne display_name)"
        created = getattr(s, "create_time", "") or ""
        print(f"  [{i}] {dn}")
        print(f"      name:    {s.name}")
        if created:
            print(f"      created: {created}")
    return stores


def list_store_contents(client, store):
    try:
        docs = list(client.file_search_stores.documents.list(parent=store.name))
    except Exception as e:
        print(f"Fehler beim Auflisten der Dokumente: {e}")
        return

    dn = getattr(store, "display_name", "") or store.name
    print(f"\nInhalt von '{dn}' ({len(docs)} Dokumente):")
    if not docs:
        return

    by_state: dict[str, list] = {}
    for d in docs:
        st = str(getattr(d, "state", "UNKNOWN")).split(".")[-1]
        by_state.setdefault(st, []).append(d)

    for st in sorted(by_state):
        print(f"\n  [{st}] {len(by_state[st])} Dokument(e):")
        for d in sorted(by_state[st], key=lambda x: getattr(x, "display_name", "") or ""):
            ddn = getattr(d, "display_name", "") or "(ohne display_name)"
            print(f"    - {ddn}")
            print(f"        {d.name}")


def delete_store(client, store) -> bool:
    dn = getattr(store, "display_name", "") or store.name
    confirm = input(f"\nFilestore '{dn}' ({store.name}) wirklich löschen? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Abgebrochen.")
        return False

    # Ohne force schlägt das Löschen bei nicht-leerem Store fehl.
    for kwargs in ({"name": store.name, "config": {"force": True}},
                   {"name": store.name, "force": True},
                   {"name": store.name}):
        try:
            client.file_search_stores.delete(**kwargs)
            print(f"Gelöscht: {store.name}")
            return True
        except TypeError:
            continue
        except Exception as e:
            print(f"Fehler beim Löschen: {e}")
            return False
    return False


def pick_store(stores, prompt: str):
    raw = input(prompt).strip()
    if not raw:
        return None
    try:
        idx = int(raw)
        return stores[idx - 1]
    except (ValueError, IndexError):
        print(f"Ungültige Auswahl: {raw}")
        return None


def pick_stores_multi(stores, prompt: str):
    raw = input(prompt).strip().lower()
    if not raw:
        return []
    if raw == "all":
        return list(stores)
    try:
        idxs = [int(x) for x in re.split(r"[,\s]+", raw) if x]
        return [stores[i - 1] for i in idxs]
    except (ValueError, IndexError):
        print(f"Ungültige Auswahl: {raw}")
        return []


def main():
    client = get_client()

    while True:
        stores = list_stores(client)

        print("\nAktionen:")
        print("  [l] Inhalt eines Stores auflisten")
        print("  [d] Store(s) löschen")
        print("  [r] Liste neu laden")
        print("  [q] Beenden")
        choice = input("Auswahl: ").strip().lower()

        if choice == "q" or choice == "":
            break
        if choice == "r":
            continue
        if not stores:
            print("Keine Stores vorhanden — nichts zu tun.")
            continue

        if choice == "l":
            store = pick_store(stores, "Nummer des Stores: ")
            if store:
                list_store_contents(client, store)
        elif choice == "d":
            targets = pick_stores_multi(
                stores,
                "Nummer(n) des/der zu löschenden Stores (z.B. '1,3' oder 'all'): "
            )
            for s in targets:
                delete_store(client, s)
        else:
            print(f"Unbekannte Aktion: {choice}")


if __name__ == "__main__":
    main()
