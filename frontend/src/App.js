// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from "react";
import axios from "axios";
// my apps:
import UsersList from "./components/Users";
import {NaviBar} from "./components/Navibar";
import {Footer} from "./components/Footer";

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = () => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users_list': []
        }
    }

    componentDidMount() {
        // собираем данные с бэк энда:
        axios.get(get_url('users/')).then(response => {
            const users_list = response.data
            this.setState(
                {
                    'users_list': response.data
                }
            )
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <NaviBar/>
                <UsersList users_list={this.state.users_list}/>
                <Footer/>
            </div>
        )
    }
}

export default App;
