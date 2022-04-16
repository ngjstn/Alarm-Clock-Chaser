// Front-end webpage design and fetch handler that sends the user's input to the backend
// Contributors: Tayyib, Sam

// React imports required
import { useState } from "react";

// Create function
const Create = () => {
    // sets the hour, minute, and song selection based on user input
    const [hour, setHour] = useState('');
    const [minute, setMinute] = useState('');
    const [song, setSong] = useState('');

    // handleSubmit function that converts the user input into an array and sends the array into the backend as JSON format.
    const handleSubmit = (e) => {
      e.preventDefault();
      const alarm = { hour, minute, song };
      fetch('http://cpen291-27.ece.ubc.ca/api/data', { // fetch command that sends it to the backend
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(alarm)
      }).then(() => {
        alert('new alarm added');
      })
    }
    // basic frontend html that allows user input
    return (
      <div className="create">
        <h2>Enter Alarm</h2>
        <form onSubmit={handleSubmit}>
          <label>hour:</label>
          <input 
            type="number" 
            required 
            value={hour}
            onChange={(e) => setHour(e.target.value)}
          />
          <label>minute:</label>
          <input
            type = "number"
            required
            value={minute}
            onChange={(e) => setMinute(e.target.value)}
          />
          <label>song:</label>
          <select
            value={song}
            onChange={(e) => setSong(e.target.value)}
          >
          <option value="Belle">None</option>
          <option value="japan">Japanese Motivation</option>
          <option value="Belle">Belle Delphine</option>
          <option value="iphone">iPhone Tone</option>
          <option value="Love">Taylor Swift: Love Stroy</option>
          <option value="DoIt">Just Do It</option>
          <option value="knowledge">Knowledge</option>
          </select>
          <button>Add Alarm</button>
        </form>
      </div>
    );
  }
   
  export default Create;