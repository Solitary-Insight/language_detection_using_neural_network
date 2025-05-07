import 'bootstrap/dist/css/bootstrap.min.css'



// Header Componenet 
import Header from './components/Header/Header';
import './components/Header/header.css';
import { STYLE_DARK, STYLE_LIGHT, ThemeData } from './utlis/constants/THEME_DATA';
import { useState } from 'react';
import About from './components/About/About';
import './components/About/about.css'
import './components/Portfolio/portfolio.css'
import Skills from './components/Skills/Skills';
import Portfolio from './components/Portfolio/Portfolio';
import Experience from './components/Experiences/Experience';
import Testimonial from './components/Testimonials/Testimonial';
import Contact from './components/Contact/Contact';
import Footer from './components/Footer/Footer';
import './index.css'
import { useThemeDetector } from './utlis/services/ThemeDetector';
import AdminPage from './Admin_Page/AdminPage';

function App() {
  const isDarkTheme = useThemeDetector((value)=>{
    enableDarkMode(value)
  });
  const [dark_mode,enableDarkMode]=useState(isDarkTheme)

  
  return (
    <ThemeData.Provider value={{style:dark_mode?STYLE_DARK:STYLE_LIGHT,darkMode:dark_mode}}>
    <div className="row p-0 m-0  " style={dark_mode?STYLE_DARK:STYLE_LIGHT}>
      
      <Header className='' enableDarkMode={enableDarkMode}></Header>
      <About/>
      <Skills/>
      <Portfolio  ></Portfolio>
      <Experience></Experience>
      <Testimonial></Testimonial>
      <Contact ></Contact>
      <Footer></Footer>
    
    </div>
    </ThemeData.Provider>
    );
}

export default App;
