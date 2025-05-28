function RouteButton({text, route, className} : {text:string, route:string, className:string}) {
    return(
        <button 
            type="button" 
            className={"btn btn-primary " + className }
            onClick={ () => window.location.href = route }>
                { text }
        </button>
    );
}

export default RouteButton;