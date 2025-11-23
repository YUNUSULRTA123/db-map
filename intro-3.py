import cartopy.crs as ccrs
import matplotlib.pyplot as plt
def create_piece_of_map(file_name = "intro_map.png"):
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()

    ny_lon, ny_lat = -75, 43
    delhi_lon, delhi_lat = 77.23, 28.61

    plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
            color='blue', linewidth=2, marker='o',
            transform=ccrs.Geodetic(),
            )

    plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
            color='gray', linestyle='--',
            transform=ccrs.PlateCarree(),
            )

    plt.text(ny_lon - 3, ny_lat - 12, 'New York',
            horizontalalignment='right',
            transform=ccrs.Geodetic())

    plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
            horizontalalignment='left',
            transform=ccrs.Geodetic())
    
    plt.savefig(file_name, dpi=300)
    plt.close()
    return file_name

if __name__ == "__main__":
    file_name = create_piece_of_map()
    print(f"График для всех классов сохранён в файл: {file_name}")
