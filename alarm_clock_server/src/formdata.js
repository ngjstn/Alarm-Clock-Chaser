import { useState } from "react";
// export function formdata() 
// {
// var time= document.getElementById("time").value;
// var song= document.getElementById("song").value;

// console.log(time + " " + song);
// alert(time);

// const retVal = [time, song];
// return retVal;
// }
// export default formdata;
const Create = () => {
    const [hour, setHour] = useState('');
    const [minute, setMinute] = useState('');
    const [song, setSong] = useState('');
  
    const handleSubmit = (e) => {
      e.preventDefault();
      const alarm = { hour, minute, song };
  
      fetch('http://localhost:8000/data', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(alarm)
      }).then(() => {
        console.log('new blog added');
      })
    }
  
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
          <option value="belle">Belle Delphine</option>
          <option value="rick">Rick Astley</option>
          </select>
          <button>Add Alarm</button>
        </form>
      </div>
    );
  }
   
  export default Create;