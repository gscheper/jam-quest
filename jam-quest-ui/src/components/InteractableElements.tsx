import React from 'react';

function RouteButton({text, route} : {text:string, route:string}) {
    return(
        <>
        <div>
            <button 
                type="button" 
                className="btn btn-primary" 
                onClick={ () => window.location.href = route }>{ text }
            </button>
        </div> 
        </>
    );
}

export default RouteButton;