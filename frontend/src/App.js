import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

const restEndpoint = "http://127.0.0.1:8000/api/v1/task/";

const callRestApi = async () => {
    const response = await fetch(restEndpoint);
    const jsonResponse = await response.json();
    console.log(jsonResponse);
    return JSON.stringify(jsonResponse);
};

function RenderResult() {
  const [apiResponse, setApiResponse] = useState("*** now loading ***");

  useEffect(() => {
      callRestApi().then(
          result => setApiResponse(result));
  },[]);

  return(
      <div>
          <h1>React App</h1>
          <p>{apiResponse}</p>
      </div>
  );
};

ReactDOM.render(
    <RenderResult/>,
    document.querySelector('#root')
);

