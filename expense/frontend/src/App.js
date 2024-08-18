import React, { useState, useMemo, useEffect } from 'react';
import styled from 'styled-components';
import bg from './img/bg1.jpg';
import { MainLayout } from './styles/Layouts';
import Orb from './Components/Orb/Orb';
import Navigation from './Components/Navigation/Navigation';
import Dashboard from './Components/Dashboard/Dashboard';
import Income from './Components/Income/Income';
import Expenses from './Components/Expenses/Expenses';
import { useGlobalContext } from './context/globalContext';

function App() {
  const [active, setActive] = useState(1);
  const { getIncomes, getExpenses } = useGlobalContext();

  // Memoize the Orb component
  const orbMemo = useMemo(() => <Orb />, []);

  // Display the correct component based on the active state
  const displayData = () => {
    switch (active) {
      case 1:
        return <Dashboard />;
      case 2:
        return <Dashboard />; // Assuming you want Dashboard for case 2 as well
      case 3:
        return <Income />;
      case 4:
        return <Expenses />;
      default:
        return <Dashboard />;
    }
  };

  // Fetch data when the component mounts or active state changes
  useEffect(() => {
    getIncomes(); // Fetch incomes
    getExpenses(); // Fetch expenses
  }, [getIncomes, getExpenses]);

  return (
    <AppStyled bg={bg} className="App">
      {orbMemo}
      <MainLayout>
        <Navigation active={active} setActive={setActive} />
        <main>
          {displayData()}
        </main>
      </MainLayout>
    </AppStyled>
  );
}

const AppStyled = styled.div`
  height: 100vh;
  background-image: url(${props => props.bg});
  background-size: cover; /* Ensure the background image covers the whole area */
  position: relative;
  display: flex; /* Use flexbox for layout */
  flex-direction: column; /* Align items in a column */
  
  main {
    flex: 1;
    background: rgba(252, 246, 249, 0.78);
    border: 3px solid #FFFFFF;
    backdrop-filter: blur(4.5px);
    border-radius: 32px;
    overflow-x: hidden;
    &::-webkit-scrollbar {
      width: 0;
    }
  }
`;

export default App;