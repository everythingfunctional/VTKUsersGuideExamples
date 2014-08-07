import vtk

cylinder = vtk.vtkCylinderSource()

cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(cylinderActor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()
