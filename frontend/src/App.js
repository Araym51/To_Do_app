import logo from './logo.svg';
import './App.css';
import React from "react";
import UsersList from "./components/Users";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        const users = [
            {
                'username': 'Araym',
                'email': 'araimo@yandex.ru',
                'first_name': 'Egor',
                'last_name': 'Ostroumov'
            },
            {
                'username': 'Olen4ik',
                'email': 'Olen4ik@yandex.ru',
                'first_name': 'Lena',
                'last_name': 'Ostroumova'
            }
        ]
        this.setState(
            {
                'users': users
            }
        )
    }

    render() {
        return (
            <div>
                <UsersList users_list={this.state.users} />
            </div>
        )

    }
}

export default App;
