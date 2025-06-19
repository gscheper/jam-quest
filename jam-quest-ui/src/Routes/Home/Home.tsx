import RouteButton from "../../components/RouteButton";
import './Home.css'

function Home() {
    return (
        <div className="grid-container">
            <img className='logo' src={'./jamquestlogo.png'}/>
            <RouteButton className='home-button' text="Quest" route="/quest"/>
            <RouteButton className='home-button' text="Login" route="http://localhost:5000/spotify_auth/login"/>
        </div>
    );
}

export default Home;