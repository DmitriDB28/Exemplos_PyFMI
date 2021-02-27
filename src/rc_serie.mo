model rc_serie
  
  parameter Real r = 1.5e3 "Resistencia";
  parameter Real c = 100e-6 "Capacitancia";
  
  Real x(start=10) "Tensao inicial";
  
  input Real u "Funcao nao homogenea";
  
  equation
    der(x) = u/(r*c) - x/(r*c);

annotation(
    __OpenModelica_simulationFlags(lv = "LOG_STATS", s = "dassl"));
end rc_serie;