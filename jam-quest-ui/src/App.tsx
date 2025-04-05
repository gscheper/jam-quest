import RouteButton from "./components/InteractableElements"
import ListGroup from "./components/ListGroup"

function App() {
  return (
        <div>
            <RouteButton text="Quest" route=""/>
            <RouteButton text="Login" route="http://localhost:5000/login"/>
        </div>
    );
}

export default App
