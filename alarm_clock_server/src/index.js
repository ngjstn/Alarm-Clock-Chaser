import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Home from './status';
import Create from './formdata';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
  <Create/>
  <Home/>
  {/* <TextBox /> 
  <App /> */}
  </React.StrictMode>,
  document.getElementById('root')
);

//Text Box component taken from: //https://www.codegrepper.com/code-examples/javascript/how+to+create+textbox+in+react

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
