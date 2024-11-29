import React from 'react';
import { Chart as ChartJS ,CategoryScale, LinearScale, BarElement, scales,} from 'chart.js/auto';
import { Bar } from 'react-chartjs-2';

//why do we need this 
ChartJS.register(CategoryScale , LinearScale , BarElement)

const BarGraphContainer = () => {
  const data = {
    labels: ['January', 'February', 'March', 'April', 'May'],
    datasets: [
      {
        label: 'Monthly Sales',
        data: [12, 19, 3, 5, 2 , 27],
        backgroundColor: [
          'rgba(75, 192, 192, 0.8)',
          'rgba(250 , 192, 19 , 0.8)',
          'rgba(253 , 135 , 135 , 0.8)',
          'rgba(43, 63 , 229 , 0.8)',
          'rgba(126, 27, 207,0.8)'
        ],
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'bottom',
      },
      title: {
        display: true,
        text: 'Sales Overview',
      },
    },
  };

  return (
    <div style={styles.graphContainer}>
      <h1 className='text-center font-semibold '>Bar chart</h1>
      <Bar data={data} options={options} />
    </div>
  );
};

const styles = {
  graphContainer: {
    padding: '16px',
    borderRadius: '15px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    backgroundColor: '#ebf2f2',
    width: '800px',
    margin: '20px auto',
    border: '1px solid #f0f0f0',
  },
};

export default BarGraphContainer;
