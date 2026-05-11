import { useEffect, useState } from "react"


export default function App() {
  const [containers, setContainers] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/containers").then(r => r.json()).then(setContainers)
  }, [])

  return (
    <div>
      <h1>Containers</h1>
      {containers.map(c => (
        <div key={c.id}>
          <b>{c.name}</b> - {c.status}
        </div>
      ))}
    </div>
  )
}