import './App.css';

//my apps:
import Navibar from "./components/Navibar";
import UsersList from "./components/Users";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";


function App() {

    return (
        <div>
            <Navibar/>
            <UsersList/>
            <ProjectList/>
            <ToDoList/>
        </div>
    );
}

export default App;
