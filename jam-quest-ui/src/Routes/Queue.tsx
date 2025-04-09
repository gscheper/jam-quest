import SongForm from "../components/Form";
import { PumpUpTheJam } from "../components/InteractableElements";

function Queue() {
    return (
        <>
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