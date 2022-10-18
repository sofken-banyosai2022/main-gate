import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Firebase 初期化
cred = credentials.Certificate('./main_gate/serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# データの更新検知
# Create an Event for notifying main thread.
callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(col_snapshot, changes, read_time):
    for change in changes:
        if (change.type.name == 'ADDED') or (change.type.name == 'MODIFIED'):
            for doc in col_snapshot:
                if doc.id == change.document.id :
                    print(doc.to_dict())
        elif change.type.name == 'REMOVED':
            callback_done.set()

col_query = db.collection(u'aaa')

# Watch the collection query
query_watch = col_query.on_snapshot(on_snapshot)
