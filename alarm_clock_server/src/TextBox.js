import './TextBox.css';
import React from 'react';
// import {formdata} from'./formdata';

class TextBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
    this.state2 = {value2: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {    this.setState({value: event.target.value});  }
  handleChange2(event) {    this.setState({value2: event.target.value});  }
  handleSubmit(event) { 
    alert('A name was submitted: ' + this.state.value);
    console.log("it works");
    event.preventDefault();
  }

  render() {
    return (
      <form>
        {/* <label>
          Time:  
          <input type="text" id="time"value={this.state.value} onChange={this.handleChange} />        </label> <br></br>
        <label>
          Song:  
          <input type="text" id="song"value={this.state2.value} onChange={this.handleChange2} />        </label> <br></br>
        <input type="submit" value="Submit" onClick={formdata}/> */}
      </form>      
    );
  }
}

export default TextBox;

