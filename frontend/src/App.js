import './App.css';
import {useQuery} from "@apollo/client";
import {useEffect, useState} from "react";
import {GET_ALL_USERS} from "./query/users";
//my apps:
import Navibar from "./components/Navibar";
import UsersList from "./components/Users";


function App() {

    return (
        <div>
            <Navibar/>
            <UsersList/>
        </div>
    );
}

export default App;
