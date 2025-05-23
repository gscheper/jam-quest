import SongForm from "../../components/Form";
import { PumpUpTheJam } from "../../components/InteractableElements";
import RedirToQuest from "../../components/RedirToQuest";
import './Queue.css';

function Queue() {
    return (
        <div className="queue-grid">
            <RedirToQuest/>
            <SongForm/>
            <PumpUpTheJam/>
        </div>
    );
}

export default Queue;