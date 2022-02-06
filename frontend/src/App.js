import logo from './logo.svg';
import './App.css';
import React from "react";
import UsersList from "./components/Users";
import axios from "axios";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users_app')
            .then(response => {
                const users_list = response.data
                this.setState(
                    {
                        'users_list': users_list
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <UsersList users_list={this.state.users}/>
            </div>
        )

    }
}

export default App;
