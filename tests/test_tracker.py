from job_search.models.schemas import TrackerStatus
from job_search.tools.tracker import TrackerStore


def test_tracker_add_update_delete(tmp_path) -> None:
    store = TrackerStore(path=tmp_path / "tracker.json")
    created = store.add("Folio3", "Junior engineer", "Python", TrackerStatus.IN_PROCESS)
    assert store.counts()["In process"] == 1
    assert store.counts()["total"] == 1

    updated = store.update(created.id, company="Folio3", status=TrackerStatus.INTERVIEW)
    assert updated is not None
    assert updated.status == TrackerStatus.INTERVIEW
    assert store.counts()["In process"] == 0
    assert store.counts()[TrackerStatus.INTERVIEW.value] == 1

    assert store.delete(created.id) is True
    assert store.list() == []
    assert store.counts()["total"] == 0
