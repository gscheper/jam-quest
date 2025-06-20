import RouteButton from '../../components/RouteButton';
import './Home.css'

function Home() {
    return (
        <div className='grid-container'>
            <img className='logo' src={'./jamquestlogo.png'}/>
            <RouteButton className='home-button' text='Quest' route='/quest'/>
            <RouteButton className='home-button' text='Login' route= {'http://' + import.meta.env.VITE_BACKEND_ENDPOINT + '/spotify_auth/login'}/>
        </div>
    );
}

export default Home;