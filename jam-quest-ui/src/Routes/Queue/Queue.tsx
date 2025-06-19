import SongForm from "../../components/Form";
import RedirToQuest from "../../components/RedirToQuest";
import './Queue.css';

function Queue() {
    return (
        <div className="queue-grid">
            <RedirToQuest/>
            <SongForm/>
        </div>
    );
}

export default Queue;