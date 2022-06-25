module main

import os
import cli


fn main() {
    mut app := cli.Command{
        name: 'pacv'
        description: 'Wrapper for pacman package manager'
        version: '5.0.0'
        execute: fn (cmd cli.Command) ? {
            println("Wrong usage. Run with --help flag to see current commands.")
            return
        }
        commands: [
            cli.Command{
                name: 'install'
                description: 'Install the desired package'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -S ${os.args[2..].join(' ')}")
                    return
                }
            }
            cli.Command{
                name: 'remove'
                description: 'Remove the desired package'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -R ${os.args[2..].join(' ')}")
                    return
                }
            }
            cli.Command{
                name: 'update'
                description: 'Updates the system'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -Syu ${os.args[2..].join(' ')}")
                    return
                }
            }
            cli.Command{
                name: 'orphans'
                description: 'Remove orphaned packages'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -R $(pacman -Qqdt)")
                    return
                }
            }
            cli.Command{
                name: 'search'
                description: 'Search for packages'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -Ss ${os.args[2..].join(' ')}")
                    return
                }
            }
            cli.Command{
                name: 'info'
                description: 'Information of packages'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -Si ${os.args[2..].join(' ')}")
                    return
                }
            }
            cli.Command{
                name: 'refresh'
                description: 'Refresh repository info'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -Syyu ${os.args[2..].join(' ')}")
                    return
                }
            }
        ]
    }
    app.setup()
    app.parse(os.args)
}