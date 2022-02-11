// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from "react";
import axios from "axios";
// my apps:
import UsersList from "./components/Users";
import {NaviBar} from "./components/Navibar";
import {Footer} from "./components/Footer";



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users_list': []
        }
    }

    componentDidMount() {
        // const users_app = [
        //     {
        //         'username': 'Araym',
        //         'email': 'araimo@yandex.ru',
        //         'first_name': 'Egor',
        //         'last_name': 'Ostroumov'
        //     },
        //     {
        //         'username': 'Olen4ik',
        //         'email': 'Olen4ik@yandex.ru',
        //         'first_name': 'Lena',
        //         'last_name': 'Ostroumova'
        //     }
        // ]
        // this.setState(
        //     {
        //         'users_app': users_app
        //     }
        // )

        // собираем данные с бэк энда:
        axios.get('http://127.0.0.1:8000/api/users_app/').then(response => {
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
