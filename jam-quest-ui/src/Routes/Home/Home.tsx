import { RouteButton } from "../../components/InteractableElements";
import './Home.css'

function Home() {
  return (
    <div className="grid-container">
        <img className='logo' src={'./jamquestlogo.png'}/>
        <RouteButton className='button' text="Quest" route="/quest"/>
        <RouteButton className='button' text="Login" route="http://localhost:5000/spotify_auth/login"/>
    </div>
    );
}

export default Home;