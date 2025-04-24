import SongForm from "../components/Form";
import { PumpUpTheJam } from "../components/InteractableElements";
import RedirToQuest from "../components/RedirToQuest";

function Queue() {
    return (
        <>
            <RedirToQuest/>
            <div>
                <PumpUpTheJam/>
            </div>
            <div>
                <SongForm/>
            </div>
        </>
    );
}

export default Queue;