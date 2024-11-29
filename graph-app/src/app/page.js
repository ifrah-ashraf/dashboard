"use client";

import dynamic from "next/dynamic";
import BarGraphContainer from "./ChartsComp/BarGraphContainer";
import DoughNutContainer from "./ChartsComp/DoughNutContainer";
import LineGraphContainer from "./ChartsComp/LineGraphContainer";


//const SimpleLineChart = dynamic(() => import("./rechartsComp/SimpleLineChart"), { ssr: false });

export default function Home() {
  return (
    <div className="flex flex-col space-y-4 items-center justify-center mt-8 mb-8">
        <BarGraphContainer/>
        <DoughNutContainer/>
        <LineGraphContainer/>
    </div>
  );
}
