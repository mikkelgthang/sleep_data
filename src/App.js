import React, { useRef, useEffect } from 'react';
import { Runtime, Inspector } from '@observablehq/runtime';
import notebook from '@mikkelgthang/sleep-app';
import './App.css';

function App() {
  return (
    <div className="sleepStatistics bg-col">
      <SleepApp></SleepApp>
    </div>
  );
}

function SleepApp() {
  const viewofSleep_viewRef = useRef();
  const viewofSleepRef = useRef();
  const viewofStat_viewRef = useRef();

  useEffect(() => {
    const runtime = new Runtime();
    runtime.module(notebook, (name) => {
      console.log(name);
      if (name === 'viewof sleep_view')
        return new Inspector(viewofSleep_viewRef.current);
      if (name === 'viewof sleep') return new Inspector(viewofSleepRef.current);
      if (name === 'viewof stat')
        return new Inspector(viewofStat_viewRef.current);
      else return true;
    });
    return () => runtime.dispose();
  }, []);

  return (
    <>
      <div className="bg-col" ref={viewofSleep_viewRef} />
      <div className="bg-col" ref={viewofSleepRef} />
      <div className="bg-col" ref={viewofStat_viewRef} />
    </>
  );
}

/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}*/

export default App;
