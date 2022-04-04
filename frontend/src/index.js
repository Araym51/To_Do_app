import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {ApolloClient, ApolloProvider, createHttpLink, InMemoryCache} from "@apollo/client";
import {setContext} from "@apollo/client/link/context";
import Cookies from "universal-cookie/es6";

const httpLink = createHttpLink({
    uri: 'http://127.0.0.1:8000/graphql/'
})

const authLink = setContext((_, {headers}) => {
    const cookies = new Cookies()
    const token =  cookies.get('token')
    console.log('index got token:', token)
    return {
        headers:{
            ...headers,
            authorization: token ? `Bearer ${token}`: "",
        }
    }
});

const client = new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
});

ReactDOM.render(
    <React.StrictMode>
        <ApolloProvider client={client}>
            <App/>
        </ApolloProvider>
    </React.StrictMode>,
    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
