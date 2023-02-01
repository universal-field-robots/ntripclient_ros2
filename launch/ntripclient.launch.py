from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, RegisterEventHandler, LogInfo, EmitEvent
from launch.event_handlers import OnProcessExit
from launch.substitutions import LaunchConfiguration, FindExecutable
from launch.events import Shutdown


def generate_launch_description():

    mountpoint = LaunchConfiguration("mountpoint")
    server = LaunchConfiguration("server")
    password = LaunchConfiguration("password")
    port = LaunchConfiguration("port")
    user = LaunchConfiguration("user")
    mode = LaunchConfiguration("mode")
    nmea = LaunchConfiguration("nmea")
    bitrate = LaunchConfiguration("bitrate")
    initudp = LaunchConfiguration("initudp")
    udpport = LaunchConfiguration("udpport")
    proxyhost = LaunchConfiguration("proxyhost")
    proxyport = LaunchConfiguration("proxyport")
    serdevice = LaunchConfiguration("serdevice")
    baud = LaunchConfiguration("baud")
    stopbits = LaunchConfiguration("stopbits")
    protocol = LaunchConfiguration("protocol")
    parity = LaunchConfiguration("parity")
    databits = LaunchConfiguration("databits")
    serlogfile = LaunchConfiguration("serlogfile")

    ntrip_client = ExecuteProcess(
        cmd=[
            FindExecutable(name='start_ntripclient'),
            "--mountpoint", mountpoint,
            "--server", server,
            "--password", password,
            "--port", port,
            "--user", user,
            "--mode", mode,
            "--nmea", nmea,
            "--bitrate", bitrate,
            "--initudp", initudp,
            "--udpport", udpport,
            "--proxyhost", proxyhost,
            "--proxyport", proxyport,
            "--serdevice", serdevice,
            "--baud", baud,
            "--stopbits", stopbits,
            "--protocol", protocol,
            "--parity", parity,
            "--databits", databits,
            "--serlogfile", serlogfile
        ],
        respawn=True
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "mountpoint", default_value=""),
        DeclareLaunchArgument(
            "server", default_value="www.euref-ip.net"),
        DeclareLaunchArgument(
            "password", default_value=""),
        DeclareLaunchArgument(
            "port", default_value="2101"),
        DeclareLaunchArgument(
            "user", default_value=""),
        DeclareLaunchArgument(
            "mode", default_value=""),
        DeclareLaunchArgument(
            "nmea", default_value=""),
        DeclareLaunchArgument(
            "bitrate", default_value=""),
        DeclareLaunchArgument(
            "initudp", default_value=""),
        DeclareLaunchArgument(
            "udpport", default_value=""),
        DeclareLaunchArgument(
            "proxyhost", default_value=""),
        DeclareLaunchArgument(
            "proxyport", default_value=""),
        DeclareLaunchArgument(
            "serdevice", default_value=""),
        DeclareLaunchArgument(
            "baud", default_value=""),
        DeclareLaunchArgument(
            "stopbits", default_value=""),
        DeclareLaunchArgument(
            "protocol", default_value=""),
        DeclareLaunchArgument(
            "parity", default_value=""),
        DeclareLaunchArgument(
            "databits", default_value=""),
        DeclareLaunchArgument(
            "serlogfile", default_value=""),
        ntrip_client,
        RegisterEventHandler(
            OnProcessExit(
                target_action=ntrip_client,
                on_exit=[
                    EmitEvent(
                        event=Shutdown(reason='NTRIPClient closed'))
                ]
            ))
    ])
