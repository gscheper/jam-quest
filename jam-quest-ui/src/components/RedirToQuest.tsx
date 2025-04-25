import axios from "axios";
axios.defaults.withCredentials=true;
axios.defaults.headers.get['Content-Type'] ='application/x-www-form-urlencoded';
axios.defaults.headers.get['Access-Control-Allow-Credentials'] ='include';

function RedirToQuest() {
    var MakeRequest = () => {
        axios({url:'http://localhost:5000/quest/king', 
               method: 'get',
               })
                .then(function (response) {
                    console.log(typeof response.data['king'])
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