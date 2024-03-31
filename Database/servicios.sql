USE [PortalDelSol]
GO

SELECT [Servicio_ID]
      ,[Servicio_Nombre]
      ,[Servicio_Precio]
  FROM [dbo].[Servicios]

GO


USE [PortalDelSol]
GO

INSERT INTO [dbo].[Servicios]
           ([Servicio_Nombre]
           ,[Servicio_Precio])
     VALUES
           (<Servicio_Nombre, varchar(255),>
           ,<Servicio_Precio, decimal(6,2),>)
GO


USE [PortalDelSol]
GO

UPDATE [dbo].[Servicios]
   SET [Servicio_Nombre] = <Servicio_Nombre, varchar(255),>
      ,[Servicio_Precio] = <Servicio_Precio, decimal(6,2),>
 WHERE <Search Conditions,,>
GO

USE [PortalDelSol]
GO

DELETE FROM [dbo].[Servicios]
      WHERE <Search Conditions,,>
GO

