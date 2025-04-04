import { useEffect, useState } from 'react'
import ContactList  from './ContactList'
import './App.css'
import ContactForm from './ContactForm'

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModelOpen, setIsModelOpen] = useState([])

  useEffect(() => {
    fetchContacts()
  }, []
  )

  const fetchContacts = async () => {
    {/* Getting response object by fetch method calling our contacts API */}
    const response = await fetch("http://127.0.0.1:5000/contacts")   
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }


  return <><ContactList contacts={contacts}/>
          <ContactForm/>
        </>
} 

export default App
