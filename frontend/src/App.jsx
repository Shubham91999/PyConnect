import { useEffect, useState } from 'react'
import ContactList  from './ContactList'
import './App.css'
import ContactForm from './ContactForm'

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModelOpen, setIsModelOpen] = useState([false])

  useEffect(() => {
    fetchContacts()
  }, []
  )

  const fetchContacts = async () => {
    {/* Getting response object by fetch method calling our contacts API */}
    const response = await fetch("http://127.0.0.1:5000/contacts")   
    const data = await response.json()
    setContacts(data.contacts) 
  }

  const closeModel = () => {
    setIsModelOpen(false)
  }

  const openCreateModel = () => {
    if (!isModelOpen) setIsModelOpen(true)
  }


  return (<>
    <ContactList contacts={contacts}/>
          <button onClick={openCreateModel}>Create New Contact</button>
          {
            isModelOpen && <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={closeModel}>&times;</span>
                  <ContactForm />
              </div>
            </div>
          }
         
        </>
  );
} 

export default App
