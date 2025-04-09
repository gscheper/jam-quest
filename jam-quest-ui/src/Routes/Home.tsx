import { RouteButton } from "../components/InteractableElements";

function Home() {
  return (
        <div>
            <RouteButton text="Quest" route="/queue"/>
            <RouteButton text="Login" route="http://localhost:5000/login"/>
        </div>
    );
}

export default Home;