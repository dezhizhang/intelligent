
import chromadb

def list_collection(db_path:str):
    client = chromadb.PersistentClient(db_path)
    collections = client.list_collections()
    print(f"chromadb:{db_path} 有{len(collections)} 个")

    for i,collection in enumerate(collections):
        print(f"collection:{i}:{collection.name} 共用{collection.count()} 条记录")

def delete_collection(dbpath,collection_name):
    try:
        client = chromadb.PersistentClient(dbpath)
        client.delete_collection(collection_name)
    except Exception as e:
        print(f"删除{collection_name} 时出错 {e}")




db_path = "../3chapter/chroma_langchain_db"
list_collection(db_path)
