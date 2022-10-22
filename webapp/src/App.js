import './App.css';
import React, {useState} from 'react';
import axios from 'axios';


/* https://www.filestack.com/fileschool/react/react-file-upload/  */
function App() {

  const [file, setFile] = useState()

  function handleChange(event) {
    setFile(event.target.files[0])
  }
  
  function handleSubmit(event) {
    event.preventDefault()
    const url ="http://0.0.0.0:5001/manager/video/add";
    const formData = new FormData();
    formData.append('file', file);
    formData.append('fileName', file.name);
    const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
    axios.post(url, formData, config).then((response) => {
      console.log(response.data);
    });

  }

  return (
    <div className="App">
        <form  method="post" methoonSubmit={handleSubmit}>
          <h1>React File Upload</h1>
          <input name="file" type="file" onChange={handleChange}/>
          <button type="submit">Upload</button>
        </form>
    </div>
  );
}

export default App;
