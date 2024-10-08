from .domain import EnqueuedSinger, Queue
from .models import EnqueuedSingerDB, QueueDB
import uuid


def to_enqueued_singer(enqueued_singer_db: EnqueuedSingerDB):
    return EnqueuedSinger(singer_id=enqueued_singer_db.singer_id,
                          position=enqueued_singer_db.queue_position)


def to_enqueued_singers(enqueued_singer_dbs: list[EnqueuedSingerDB]):
    return [to_enqueued_singer(es) for es in enqueued_singer_dbs]


def to_enqueued_singer_db(queue_id: uuid.UUID, enqueued_singer: EnqueuedSinger):
    return EnqueuedSingerDB(str(queue_id), 
                            enqueued_singer.position, 
                            singer_id=str(enqueued_singer.singer_id))


def to_enqueued_singer_dbs(queue_id: uuid.UUID, enqueued_singers: EnqueuedSinger):
    return [to_enqueued_singer_db(queue_id, es) for es in enqueued_singers]


def to_queue_db(queue: Queue):
    return QueueDB(str(queue.queue_id),
                   location_id = str(queue.location_id),
                   event_date = queue.event_date,
                   current_singer_index = queue.current_singer_index)