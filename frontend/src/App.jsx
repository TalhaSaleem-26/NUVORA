import { useState } from "react"


function App() {
  const [count,setCount]=useState(0)
  return (
    <div className="bg-grey-500 m-5 w-100 h-200 ">

<p><h1>Count Value</h1>{count}</p>

<button className="bg-grey-600 m-5" onClick={()=>setCount(count+1)}>Increase </button>
<button className="m-5 p-4" onClick={()=>setCount(0)}>Reset Count Value</button>
    </div>
  )
}

export default App