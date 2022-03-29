import './App.css';
import {Route, Switch, BrowserRouter,} from "react-router-dom";
//my apps:
import Navibar from "./components/Navibar";
import UsersList from "./components/Users";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import NotFound404 from "./components/NotFound404";
import Home from "./components/Home";


function App() {

    return (
        <div>
            <Navibar/>
            <BrowserRouter>
                <Switch>
                    <Route exact path='/' component={() => <Home/>}/>
                    <Route exact path='/users' component={() => <UsersList/>}/>
                    <Route exact path='/projects' component={() => <ProjectList/>}/>
                    <Route exact path='/todo' component={() => <ToDoList/>}/>
                    <Route component={NotFound404}/>
                </Switch>
            </BrowserRouter>
        </div>
    );
}

export default App;
