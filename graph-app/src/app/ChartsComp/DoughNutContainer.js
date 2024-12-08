import { Doughnut } from "react-chartjs-2";
import { ScoolData } from "../utils/data";

const DoughNutContainer = () => {
    let oddSchoolNum = 0
    let StandSchool = 0

    ScoolData.map((val)=> {
        if(val.Result == "ODD"){
            oddSchoolNum++
        }else{
            StandSchool++
        }
    })
    /* if (typeof window === 'undefined') {
        console.log('Logging from the server:', oddSchoolNum , StandSchool);
      } else {
        console.log('Logging from the client:', "Hi buddy");
      } */
      
    const data = {
        labels: ['Odd School', 'Standard School'],
        datasets: [
            {
                label: 'school structure',
                data: [oddSchoolNum , StandSchool],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(250 , 192, 19 , 0.8)',
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
                text: 'School Structure',
            },
        },
    };

    return (
        <div style={styles.graphContainer}>
            <h1 className='text-center font-semibold '>Doughnut</h1>
            <Doughnut data={data} options={options} />
        </div>
    )
}

const styles = {
    graphContainer: {
        padding: '16px',
        borderRadius: '15px',
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
        backgroundColor: '#ebf2f2',
        width: '600px',
        height: '600px',
        margin: '16px auto',
        border: '1px solid #f0f0f0',
    },
};

export default DoughNutContainer