import React, { useState } from "react";
import { upload_file } from "../services/api";
// import '../styles/App.css'
const FileUploads = ({setLoading}) => {
     const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  async function handleUpload(){
    if (file) {
      setLoading(true)
    //   alert(`Uploading: ${file.name}`);
      const formData = new FormData();
      formData.append("file", file); 
        const resonse = await upload_file(formData)
        console.log(resonse);
        if (resonse){
          setLoading(false);
        }
      // Add your upload logic here
    } else {
      alert("Please select a file first!");
    }
  };

  return (
    <div className="card">
      <h3 className="card-title">Upload Your File</h3>
      <input type="file" onChange={handleFileChange} />
      {file && <p>Selected File: {file.name}</p>}
      <button className="upload-btn" onClick={handleUpload}>
        Upload
      </button>
    </div>
  );
}

export default FileUploads