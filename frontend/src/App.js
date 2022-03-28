import './App.css';

//my apps:
import Navibar from "./components/Navibar";
import UsersList from "./components/Users";
import ProjectList from "./components/Projects";


function App() {

    return (
        <div>
            <Navibar/>
            {/*<UsersList/>*/}
            <ProjectList/>
        </div>
    );
}

export default App;
