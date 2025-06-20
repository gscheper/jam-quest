import axios from "axios";
axios.defaults.withCredentials=true;
axios.defaults.headers.get['Content-Type'] ='application/x-www-form-urlencoded';
axios.defaults.headers.get['Access-Control-Allow-Credentials'] ='include';

function RedirToQuest() {
    var MakeRequest = () => {
        axios({url:'http://' + import.meta.env.VITE_BACKEND_ENDPOINT + '/quest/king', 
               method: 'get',
               })
                .then(function (response) {
                    if (response.data['king'] === false) {
                        window.location.href = "/quest";
                    }
                    })
                .catch(function (error) {console.log(error);});
    };

    MakeRequest();
    return (<></>);
}
  
export default RedirToQuest;