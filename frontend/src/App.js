// import logo from './logo.svg';
import './App.css';
import React from "react";
import UsersList from "./components/Users";
import axios from "axios";

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
                <UsersList users_list={this.state.users_list}/>
            </div>
        )

    }
}

export default App;
