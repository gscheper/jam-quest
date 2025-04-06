import { RouteButton } from "./components/InteractableElements";

function App() {
  return (
        <div>
            <RouteButton text="Quest" route="/queue.html"/>
            <RouteButton text="Login" route="http://localhost:5000/login"/>
        </div>
    );
}

export default App
