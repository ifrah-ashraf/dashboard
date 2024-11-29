import { Pie, PieChart } from "recharts";

const PieGraph = () => {
  const data1 = [
    {
      "name": "Group A",
      "value": 400
    },
    {
      "name": "Group B",
      "value": 300
    },
    {
      "name": "Group C",
      "value": 300
    },
    {
      "name": "Group D",
      "value": 200
    },
    {
      "name": "Group E",
      "value": 278
    },
    {
      "name": "Group F",
      "value": 189
    }
  ];
  return (
    <PieChart width={730} height={250}>
      <Pie data={data1} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={50} fill="blue" />
    </PieChart>
  )

}

export default PieGraph;